package ar.edu.itba.sia.gps;

import java.util.*;

import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.Problem;
import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import static ar.edu.itba.sia.gps.SearchStrategy.IDDFS;

public class GPSEngine {

	private Deque<GPSNode> open;
	private Map<State, Integer> bestCosts;
	private Problem problem;
	private long explosionCounter;
	private boolean finished;
	private boolean failed;
	private GPSNode solutionNode;
	private Optional<Heuristic> heuristic;
	private long startTime, endTime;
	private int statesAnalyzed, frontierNodes;

	// Use this variable in open set order.
	protected SearchStrategy strategy;

	public GPSEngine(Problem problem, SearchStrategy strategy, Heuristic heuristic) {
		open = new ArrayDeque<>();
		bestCosts = new HashMap<>();
		this.problem = problem;
		this.strategy = strategy;
		this.heuristic = Optional.ofNullable(heuristic);
		explosionCounter = 0;
		statesAnalyzed = 0;
		frontierNodes = 0;
		finished = false;
		failed = false;
	}

	public void findSolution() {
		startTime = System.currentTimeMillis();
		GPSNode rootNode = new GPSNode(problem.getInitState(), 0, null);

		open.add(rootNode);
		// TODO: ¿Lógica de IDDFS?
		if(strategy == IDDFS){
			int limitDepth = 0;
			while(!finished) {
				GPSNode currentNode = open.pop();
				if (currentNode.getDepth() == limitDepth) {
					if (problem.isGoal(currentNode.getState())){
						finished = true;
						solutionNode = currentNode;
						endTime = System.currentTimeMillis();
						return;
					} else if (open.isEmpty()){
						open.push(rootNode);
						limitDepth++;
					}
				} else if(currentNode.getDepth() == limitDepth-1){
					explode(currentNode);
				}
			}
		} else {
			while (open.size() > 0) {
				GPSNode currentNode = open.remove();
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
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
			for (GPSNode newNode:newCandidates) {
				open.push(newNode);
			}
			break;
		case GREEDY:
			newCandidates = new PriorityQueue<>(Comparator.comparingInt(n -> heuristic.get().getValue(n.getState())));
			addCandidates(node, newCandidates);
			open.addAll(newCandidates);
			break;
		case ASTAR:
			if (!isBest(node.getState(), node.getCost())) {
				return;
			}
			newCandidates = new ArrayList<>();
			addCandidates(node, newCandidates);
//			for (GPSNode newNode:newCandidates) {
//				open.push(newNode);
//			}
			break;
		}
	}

	private void addCandidates(GPSNode node, Collection<GPSNode> candidates) {
		explosionCounter++;
		updateBest(node);
		for (Rule rule : problem.getRules()) {
			Optional<State> newState = rule.apply(node.getState());
			statesAnalyzed++;
			if (newState.isPresent()) {
				frontierNodes++;
				GPSNode newNode = new GPSNode(newState.get(), node.getCost() + rule.getCost(), rule);
				newNode.setParent(node);
				candidates.add(newNode);
			}
		}
	}

	private boolean isBest(State state, Integer cost) {
		return !bestCosts.containsKey(state) || cost < bestCosts.get(state);
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
