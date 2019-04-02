package ar.edu.itba.sia.gps;
import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.Problem;
import ar.edu.itba.sia.gps.api.State;
import ar.edu.itba.sia.gps.model.*;
import org.apache.commons.cli.*;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.awt.*;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.List;

import org.json.simple.parser.ParseException;

public class Main {

    public static void main(String[] args) {
        Options options = new Options();

        Option heuristic1 = new Option("h1", "heuristic1", false, "Heuristic function used h1");
        options.addOption(heuristic1);

        Option heuristic2 = new Option("h2", "heuristic2", false, "Heuristic function used h2");
        options.addOption(heuristic2);

        Option board = new Option("b", "board", true, "Path to json file with initial board state");
        board.setRequired(true);
        options.addOption(board);

        Option algorithm = new Option("a", "algorithm", true,
                "Search algorithm used (BFS, DFS, IDDFS, Greedy, A*)");
        algorithm.setRequired(true);
        options.addOption(algorithm);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();

        boolean hasHeuristic1 = false;
        boolean hasHeuristic2 = false;
        String initialBoardPath = "";
        String searchStrategyChosenString = "BFS";

        try {

            CommandLine cmd;
            cmd = parser.parse(options, args);
            hasHeuristic1 = cmd.hasOption("h1");
            hasHeuristic2 = cmd.hasOption("h2");
            initialBoardPath = cmd.getOptionValue("board");
            searchStrategyChosenString = cmd.getOptionValue("algorithm");

        } catch (org.apache.commons.cli.ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name", options);

            System.exit(1);
        }

        SearchStrategy searchStrategyChosen = SearchStrategy.valueOf(searchStrategyChosenString.toUpperCase());
        Heuristic heuristicChosen = parseHeuristic(hasHeuristic1, hasHeuristic2, searchStrategyChosen);
        Problem problemChosen = new ProblemImpl(parseBoard(initialBoardPath));

        printArguments(searchStrategyChosenString, heuristicChosen);

        GPSEngine engine = new GPSEngine(problemChosen, searchStrategyChosen, heuristicChosen);

        engine.findSolution();

        printSolution(engine);
    }

    private static void printArguments(String searchStrategy, Heuristic heuristic) {
        System.out.println("Search strategy chosen: " + searchStrategy);
        System.out.print("Heuristic chosen: ");

        if(heuristic == null)
            System.out.println("none");
        else if(heuristic.getClass().equals(LinearDistanceHeuristic.class))
            System.out.println("Linear distance heuristic");
    }

    private static Heuristic parseHeuristic(boolean hasHeuristic1, boolean hasHeuristic2, SearchStrategy searchStrategy) {
        if(hasHeuristic1) {
            if(hasHeuristic2)
                throw new IllegalArgumentException("Only one heuristic allowed");

            return new LinearDistanceHeuristic();
        }

        if(!hasHeuristic2 && (searchStrategy == SearchStrategy.GREEDY || searchStrategy == SearchStrategy.ASTAR))
            throw new IllegalArgumentException("Need heuristic for this search strategy");

//        return la otra heuristica
        return null;
    }

    private static State parseBoard(String path) {

        JSONParser jsonParser = new JSONParser();
        JSONObject state = new JSONObject();

        try (FileReader reader = new FileReader(path)) {

            Object obj = jsonParser.parse(reader);
            state = (JSONObject) obj;

        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }

        JSONArray JSONSquareList = (JSONArray) state.get("squares");
        JSONArray JSONCircleList = (JSONArray) state.get("circles");
        JSONArray board = (JSONArray) state.get("board");

        Map<Point, Square> squareList = new HashMap<>();
        Map<Point, Circle> circleList = new HashMap<>();

        for (Object square : JSONSquareList) {
            JSONObject currentSquare = (JSONObject) square;
            Map.Entry<Point, Square> entry = parseSquare(currentSquare, board);

            if(entry != null)
                squareList.put(entry.getKey(), entry.getValue());
        }

        for (Object circle:JSONCircleList) {
            JSONObject currentCircle = (JSONObject) circle;
            Map.Entry<Point, Circle> entry = parseCircle(currentCircle, board);

            if(entry != null)
                circleList.put(entry.getKey(), entry.getValue());
        }

        checkValidBoard(squareList, circleList);

        return new StateImpl(squareList, circleList, board.size());
    }

    private static Map.Entry<Point, Square> parseSquare(JSONObject JSONSquare, JSONArray board) {

        String squareName = (String) JSONSquare.get("name");
        Direction direction = Direction.valueOf(((String) JSONSquare.get("direction")).toUpperCase());
        String color = (String) JSONSquare.get("color");

        Point position = getBoardPosition(squareName, board);

        if(position == null)
            return null;

        return new AbstractMap.SimpleEntry<>(position, new Square(color, direction));
    }

    private static Map.Entry<Point, Circle> parseCircle(JSONObject JSONCircle, JSONArray board) {
        String circleName = (String) JSONCircle.get("name");
        String color = (String) JSONCircle.get("color");

        Point position = getBoardPosition(circleName, board);

        if(position == null)
            return null;

        return new AbstractMap.SimpleEntry<>(position, new Circle(color));
    }

    private static Point getBoardPosition(String name, JSONArray board) {

        for (int i = 0; i < board.size(); i++) {

            for (int j = 0; j < ((JSONArray) board.get(i)).size(); j++) {

                String cell = (String)((JSONArray) board.get(i)).get(j);
                if(name.equals(cell))
                    return new Point(i, j);
            }
        }

        return null;
    }

    private static void checkValidBoard(Map<Point, Square> squares, Map<Point, Circle> circles) {
        Map<String, Point> squareColors = new HashMap<>();
        Map<String, Point> circleColors = new HashMap<>();

        List<String> squareColorsList = new ArrayList<>();
        List<String> circleColorsList = new ArrayList<>();


        for (Map.Entry<Point, Square> entry: squares.entrySet()){
            squareColors.put(entry.getValue().getColor(), entry.getKey());
            squareColorsList.add(entry.getValue().getColor());
        }

        for (Map.Entry<Point, Circle> entry: circles.entrySet()){
            circleColors.put(entry.getValue().getColor(), entry.getKey());
            circleColorsList.add(entry.getValue().getColor());
        }

        Set<String> appeared = new HashSet<>();

        for (String color: squareColorsList) {
            if (!appeared.add(color)) {
                throw new IllegalArgumentException("Board is invalid, can't have two squares with the same color.");
            }
        }

        appeared.clear();

        for (String color: circleColorsList) {
            if (!appeared.add(color)) {
                throw new IllegalArgumentException("Board is invalid, can't have two circles with the same color.");
            }
        }

        for (Map.Entry<String, Point> entry : squareColors.entrySet()){
            if(circleColors.get(entry.getKey()) == null)
                throw new IllegalArgumentException("Board is invalid, should have one square and one circle of each color and don't repeat names.");
        }

        for (Map.Entry<String, Point> entry : circleColors.entrySet()){
            if(squareColors.get(entry.getKey()) == null)
                throw new IllegalArgumentException("Board is invalid, should have one square and one circle of each color and don't repeat names.");
        }


    }

    private static void printSolution(GPSEngine engine) {
        System.out.println("Your search to solution was " + (engine.isFailed() ? "unsuccessful" : "successful"));

        System.out.println("Nodes expanded: " + engine.getExplosionCounter());

        System.out.println("States analyzed: " + engine.getStatesAnalyzed());

        System.out.println("Frontier nodes: " + engine.getFrontierNodes());

        if(!engine.isFailed()) {

            System.out.println("Solution depth and cost: " + engine.getSolutionNode().getCost());

            System.out.println("Your path to reach the solution was:");
            printPathToSolution(engine.getSolutionNode());

            System.out.println("It took " + (engine.getEndTime() - engine.getStartTime()) + " ms.");
        }
    }

    private static void printPathToSolution(GPSNode currentNode) {
        if(currentNode.getParent() == null){
            System.out.println(currentNode.getState().getRepresentation());
            return;
        }

        printPathToSolution(currentNode.getParent());

        System.out.println(currentNode.getGenerationRule().getName());
        System.out.println(currentNode.getState().getRepresentation());
    }
}
