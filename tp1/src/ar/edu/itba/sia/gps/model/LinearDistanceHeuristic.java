package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.*;
import java.util.List;

public class LinearDistanceHeuristic implements Heuristic {

    public LinearDistanceHeuristic() {
    }

    @Override
    public Integer getValue(State state) {
        StateImpl stateImplementation = (StateImpl) state;
        Map<Point, Circle> circles = stateImplementation.getCircles();
        Map<String, Point> circlePointMap = new HashMap<>();

        for (Map.Entry<Point, Circle> circleEntry:circles.entrySet()) {
            circlePointMap.put(circleEntry.getValue().getColor(), circleEntry.getKey());
        }

        List<Double> values = new ArrayList<>();

        for (Map.Entry<Point, Square> squareEntry : stateImplementation.getSquares().entrySet()) {
            Point squarePosition = squareEntry.getKey();

            Point circlePosition = circlePointMap.get(squareEntry.getValue().getColor());

            Double value = Math.sqrt(Math.pow(circlePosition.getX() - squarePosition.getX(), 2) +
                    Math.pow(circlePosition.getY() - squarePosition.getY(),2));

            values.add(value);
        }

        return Collections.max(values).intValue();
    }
}
