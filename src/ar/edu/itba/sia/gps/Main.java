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
//    arguments: json board, heuristic, algorithm used
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

        String heuristicChosenString1 = "";
        String heuristicChosenString2 = "";
        String initialBoardPath = "";
        String searchStrategyChosenString = "BFS";

        try {

            CommandLine cmd;
            cmd = parser.parse(options, args);
            heuristicChosenString1 = cmd.getOptionValue("heuristic1");
            heuristicChosenString2 = cmd.getOptionValue("heuristic2");
            initialBoardPath = cmd.getOptionValue("board");
            searchStrategyChosenString = cmd.getOptionValue("algorithm");

        } catch (org.apache.commons.cli.ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name", options);

            System.exit(1);
        }

        SearchStrategy searchStrategyChosen = SearchStrategy.valueOf(searchStrategyChosenString);
        Heuristic heuristicChosen = parseHeuristic(heuristicChosenString1, heuristicChosenString2, searchStrategyChosen);
        Problem problemChosen = new ProblemImpl(parseBoard(initialBoardPath));

        GPSEngine engine = new GPSEngine(problemChosen, searchStrategyChosen, heuristicChosen);

        engine.findSolution();

        printSolution(engine);
    }

    private static Heuristic parseHeuristic(String heuristic1, String heuristic2, SearchStrategy searchStrategy) {
        if(heuristic1 != null) {
            if(heuristic2 != null)
                throw new IllegalArgumentException("Only one heuristic allowed");

            return new LinearDistanceHeuristic();
        }
        if(heuristic2 == null && (searchStrategy == SearchStrategy.GREEDY || searchStrategy == SearchStrategy.ASTAR))
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
            squareList.put(entry.getKey(), entry.getValue());
        }

        for (Object circle:JSONCircleList) {
            JSONObject currentCircle = (JSONObject) circle;
            Map.Entry<Point, Circle> entry = parseCircle(currentCircle, board);
            circleList.put(entry.getKey(), entry.getValue());
        }

        return new StateImpl(squareList, circleList, board.size());
    }

    private static Map.Entry<Point, Square> parseSquare(JSONObject JSONSquare, JSONArray board) {

        String squareName = (String) JSONSquare.get("name");
        Direction direction = Direction.valueOf((String) JSONSquare.get("direction"));
        String color = (String) JSONSquare.get("color");

        Point position = getBoardPosition(squareName, board);

        return new AbstractMap.SimpleEntry<>(position, new Square(color, direction));
    }

    private static Map.Entry<Point, Circle> parseCircle(JSONObject JSONCircle, JSONArray board) {
        String circleName = (String) JSONCircle.get("name");
        String color = (String) JSONCircle.get("color");

        return new AbstractMap.SimpleEntry<>(getBoardPosition(circleName, board), new Circle(color));
    }

    private static Point getBoardPosition(String name, JSONArray board) {

        for (int i = 0; i < board.size(); i++) {

            for (int j = 0; j < ((JSONArray) board.get(i)).size(); j++) {

                String cell = (String)((JSONArray) board.get(i)).get(j);
                if(name.equals(cell))
                    return new Point(i, j);
            }
        }

        return new Point();
    }

    private static void printSolution(GPSEngine engine) {
        System.out.println("Your search to solution was " + (engine.isFailed() ? "unsuccessful." : "successful."));

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
