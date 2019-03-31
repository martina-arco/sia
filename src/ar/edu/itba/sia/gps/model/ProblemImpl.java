package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Problem;
import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;


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

        Map<Point, Circle> circleMap = state.getCircles();

        for (Map.Entry<Point, Square> entry: state.getSquares().entrySet()) {
            Point position = entry.getKey();
            Circle circle = circleMap.get(position);
            if(circle == null || !entry.getValue().getColor().equals(circle.getColor()))
                return false;
        }

        return true;
    }

    @Override
    public List<Rule> getRules() {
        List<Rule> rules = new ArrayList<>();

        for (Square square:initialState.getSquares().values())
            rules.add(new RuleImpl(square));

        return rules;
    }
}
