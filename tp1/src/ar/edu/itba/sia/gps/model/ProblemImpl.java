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

        StateImpl stateImplementation = (StateImpl) state;

        Map<Point, Circle> circleMap = stateImplementation.getCircles();

        for (Map.Entry<Point, Square> entry: stateImplementation.getSquares().entrySet()) {
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

        for (Square square : ((StateImpl)initialState).getSquares().values())
            rules.add(new RuleImpl(square));

        return rules;
    }
}
