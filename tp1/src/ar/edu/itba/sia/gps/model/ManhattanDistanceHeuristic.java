package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.*;
import java.util.List;

public class ManhattanDistanceHeuristic implements Heuristic {

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

            Double value = Math.abs(circlePosition.getX() - squarePosition.getX()) + Math.abs(circlePosition.getY() - squarePosition.getY());

            values.add(value);
        }

        return Collections.max(values).intValue();
    }
}
