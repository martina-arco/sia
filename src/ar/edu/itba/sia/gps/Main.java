package ar.edu.itba.sia.gps;
import org.apache.commons.cli.*;

public class Main {
//    arguments: json board, heuristic, algorithm used
    public static void main(String[] args) {
        Options options = new Options();

        Option heuristic = new Option("h", "heuristic", true, "heuristic function used");
        heuristic.setRequired(true);
        options.addOption(heuristic);

        Option board = new Option("b", "board", true, "initial board state");
        board.setRequired(true);
        options.addOption(board);

        Option algorithm = new Option("a", "algorithm", true,
                "search algorithm used (BFS, DFS, IDDFS, greedy, A*)");
        algorithm.setRequired(true);
        options.addOption(algorithm);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();

        String heuristicChosen;
        String initialBoardPath;
        String algorithmChosen;

        try {

            CommandLine cmd;
            cmd = parser.parse(options, args);
            heuristicChosen = cmd.getOptionValue("heuristic");
            initialBoardPath = cmd.getOptionValue("board");
            algorithmChosen = cmd.getOptionValue("algorithm");

        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("utility-name", options);

            System.exit(1);
        }




        System.out.println("lalallalal");
    }

    public void parseHeuristic(String heuristic) {

    }

    public void parseBoard(String path) {

    }

    public void parseAlgorithm(String algorithm) {

    }
}
