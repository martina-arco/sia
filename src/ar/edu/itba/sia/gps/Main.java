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

        Option heuristic = new Option("h", "heuristic", true, "Heuristic function used (h1, h2)");
//        heuristic.setRequired(true);
        options.addOption(heuristic);

        Option board = new Option("b", "board", true, "Path to json file with initial board state");
        board.setRequired(true);
        options.addOption(board);

        Option algorithm = new Option("a", "algorithm", true,
                "Search algorithm used (BFS, DFS, IDDFS, Greedy, A*)");
        algorithm.setRequired(true);
        options.addOption(algorithm);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();

        String heuristicChosenString = "h1";
        String initialBoardPath = "";
        String searchStrategyChosenString = "BFS";

        try {

            CommandLine cmd;
            cmd = parser.parse(options, args);
            heuristicChosenString = cmd.getOptionValue("heuristic");
            initialBoardPath = cmd.getOptionValue("board");
            searchStrategyChosenString = cmd.getOptionValue("algorithm");

        } catch (org.apache.commons.cli.ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name", options);

            System.exit(1);
        }

        Heuristic heuristicChosen = new LinearDistanceHeuristic();

        if(heuristicChosenString != null)
            heuristicChosen = parseHeuristic(heuristicChosenString);

        SearchStrategy searchStrategyChosen = SearchStrategy.valueOf(searchStrategyChosenString);
        Problem problemChosen = new ProblemImpl(parseBoard(initialBoardPath));

        GPSEngine engine = new GPSEngine(problemChosen, searchStrategyChosen, heuristicChosen);

        engine.findSolution();
    }

    private static Heuristic parseHeuristic(String heuristic) {
        switch (heuristic) {
            case "h1":
                return new LinearDistanceHeuristic();
        }
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

        return new AbstractMap.SimpleEntry<Point, Square>(getBoardPosition(squareName, board), new Square(color, direction));
    }

    private static Map.Entry<Point, Circle> parseCircle(JSONObject JSONCircle, JSONArray board) {
        String circleName = (String) JSONCircle.get("name");
        String color = (String) JSONCircle.get("color");

        return new AbstractMap.SimpleEntry<Point, Circle>(getBoardPosition(circleName, board), new Circle(color));
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
}
