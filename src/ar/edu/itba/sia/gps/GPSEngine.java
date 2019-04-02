package ar.edu.itba.sia.gps;

import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.Problem;
import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.util.*;

import static ar.edu.itba.sia.gps.SearchStrategy.ASTAR;
import static ar.edu.itba.sia.gps.SearchStrategy.IDDFS;

public class GPSEngine {

	private Deque<GPSNode> open;
	private PriorityQueue<GPSNode> openList;
	private HashSet<GPSNode> closedList;
	private Map<State, Integer> bestCosts;
	private Problem problem;
	private long explosionCounter;
	private boolean finished;
	private boolean failed;
	private HashSet<State> depthLimited;
	private GPSNode solutionNode;
	private Optional<Heuristic> heuristic;
	private long startTime, endTime;
	private int statesAnalyzed, frontierNodes, limitDepth;

	// Use this variable in open set order.
	protected SearchStrategy strategy;

	public GPSEngine(Problem problem, SearchStrategy strategy, Heuristic heuristic) {
		open = new ArrayDeque<>();
		closedList = new HashSet<>();
		bestCosts = new HashMap<>();
		this.problem = problem;
		this.strategy = strategy;
		this.heuristic = Optional.ofNullable(heuristic);
		openList = new PriorityQueue<>(Comparator.comparingInt(nodeToAnalyze -> nodeToAnalyze.getCost() + this.heuristic.get().getValue(nodeToAnalyze.getState())));
		explosionCounter = 0;
		statesAnalyzed = 0;
		frontierNodes = 0;
		limitDepth = 0;
		finished = false;
		failed = false;
		depthLimited = new HashSet<>();
	}

	public void findSolution() {
		startTime = System.currentTimeMillis();
		GPSNode rootNode = new GPSNode(problem.getInitState(), 0, null, 0);
		open.add(rootNode);
		if (strategy == ASTAR)
			openList.add(rootNode);
		while (open.size() > 0) {
			if (strategy == IDDFS) {
				GPSNode currentNode = open.pop();
				if (currentNode.getDepth() == limitDepth) {
					statesAnalyzed++;
					if (isBest(currentNode.getState(), currentNode.getCost())) {
						depthLimited.add(currentNode.getState());

						if (problem.isGoal(currentNode.getState())) {
							finished = true;
							solutionNode = currentNode;
							endTime = System.currentTimeMillis();
							return;
						}
					}
				} else {
					explode(currentNode);
				}

				if (open.isEmpty() && !depthLimited.isEmpty()) {
					open.push(rootNode);
					limitDepth++;
					depthLimited.clear();
					bestCosts.clear();
				}
			} else if(strategy == ASTAR){
				if(openList.isEmpty()) {
					open.remove();
					break;
				}
				GPSNode currentNode = openList.remove();
				closedList.add(currentNode);
				statesAnalyzed++;
				if (problem.isGoal(currentNode.getState())) {
					finished = true;
					solutionNode = currentNode;
					endTime = System.currentTimeMillis();
					return;
				} else {
					explode(currentNode);
				}
			} else {
				GPSNode currentNode = open.remove();
				statesAnalyzed++;
				if (problem.isGoal(currentNode.getState())) {
					finished = true;
					solutionNode = currentNode;
					endTime = System.currentTimeMillis();
					return;
				} else {
					explode(currentNode);
				}
			}
		}
		failed = true;
		finished = true;
	}

	private void explode(GPSNode node) {
		Collection<GPSNode> newCandidates;
		switch (strategy) {
		case BFS:
			if (bestCosts.containsKey(node.getState())) {
				return;
			}
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
			open.addAll(newCandidates);
			break;
		case DFS:
			if (bestCosts.containsKey(node.getState())) {
				return;
			}
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
			for (GPSNode newNode:newCandidates) {
				open.push(newNode);
			}
			break;
		case IDDFS:
			if (!isBest(node.getState(), node.getCost()))
				return;
			depthLimited.remove(node.getState());
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
			for (GPSNode newNode:newCandidates) {
				open.push(newNode);
			}
			break;
		case GREEDY:
			if (bestCosts.containsKey(node.getState())) {
				return;
			}
			newCandidates = new PriorityQueue<>(Comparator.comparingInt(nodeToAnalyze -> -heuristic.get().getValue(nodeToAnalyze.getState())));
			addCandidates(node, newCandidates);
			while(!newCandidates.isEmpty()) {
				open.addFirst(((PriorityQueue<GPSNode>) newCandidates).poll());
			}
			break;
		case ASTAR:
			if(!isBest(node.getState(), node.getCost() + heuristic.get().getValue(node.getState())))
				return;
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
			for (GPSNode newNode:newCandidates) {
				if(!closedList.contains(newNode)){
					openList.add(newNode);
				}
			}
			break;
		}
	}

	private void addCandidates(GPSNode node, Collection<GPSNode> candidates) {
		explosionCounter++;
		updateBest(node);
		for (Rule rule : problem.getRules()) {
			Optional<State> newState = rule.apply(node.getState());
			if (newState.isPresent()) {
				frontierNodes++;
				GPSNode newNode = new GPSNode(newState.get(), node.getCost() + rule.getCost(), rule, node.getDepth()+1);
				newNode.setParent(node);
				candidates.add(newNode);
			}
		}
	}

	private boolean isBest(State state, Integer cost) {
		return !bestCosts.containsKey(state) || cost < bestCosts.get(state);
	}

	private boolean isBestOrSame(State state, Integer cost) {
		return !bestCosts.containsKey(state) || cost <= bestCosts.get(state);
	}

	private void updateBest(GPSNode node) {
		if(strategy.equals(SearchStrategy.ASTAR))
			bestCosts.put(node.getState(), node.getCost() + heuristic.get().getValue(node.getState()));
		else
			bestCosts.put(node.getState(), node.getCost());
	}

	// GETTERS FOR THE PEOPLE!

	public Queue<GPSNode> getOpen() {
		return open;
	}

	public Map<State, Integer> getBestCosts() {
		return bestCosts;
	}

	public Problem getProblem() {
		return problem;
	}

	public long getExplosionCounter() {
		return explosionCounter;
	}

	public boolean isFinished() {
		return finished;
	}

	public boolean isFailed() {
		return failed;
	}

	public GPSNode getSolutionNode() {
		return solutionNode;
	}

	public SearchStrategy getStrategy() {
		return strategy;
	}

	public long getStartTime() {
		return startTime;
	}

	public long getEndTime() {
		return endTime;
	}

	public int getStatesAnalyzed() {
		return statesAnalyzed;
	}

	public int getFrontierNodes() {
		return frontierNodes;
	}
}
