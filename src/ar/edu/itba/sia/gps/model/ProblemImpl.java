package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Problem;
import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class ProblemImpl implements Problem {

    private State initialState;

    public ProblemImpl(State initialState) {
        this.initialState = initialState;
    }

    @Override
    public State getInitState() {
        return initialState;
    }

    @Override
    public boolean isGoal(State state) {

        List<Square> squares = state.getSquares();
        List<Circle> circles = state.getCircles();

        Map<String, Point> squarePositionsByColor = squares.stream().collect(Collectors.toMap(Square::getColor, Square::getPosition));
        Map<String, Point> circlePositionsByColor = circles.stream().collect(Collectors.toMap(Circle::getColor, Circle::getPosition));

        for (String color : squarePositionsByColor.keySet()) {
            if(!circlePositionsByColor.get(color).equals(squarePositionsByColor.get(color)))
                return false;
        }

        return true;
    }

    @Override
    public List<Rule> getRules() {
//        for (Figure figure:initialState.getFigures()) {
//
//        }
        return null;
    }
}
