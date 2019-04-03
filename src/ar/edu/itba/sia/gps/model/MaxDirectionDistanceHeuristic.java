package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Heuristic;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.*;
import java.util.List;

public class MaxDirectionDistanceHeuristic implements Heuristic {

    @Override
    public Integer getValue(State state) {
        StateImpl stateImplementation = (StateImpl) state;
        Map<Point, Circle> circles = stateImplementation.getCircles();
        Map<String, Point> circlePointMap = new HashMap<>();

        for (Map.Entry<Point, Circle> circleEntry:circles.entrySet()) {
            circlePointMap.put(circleEntry.getValue().getColor(), circleEntry.getKey());
        }

        List<Double> valuesForUp = new ArrayList<>();
        List<Double> valuesForDown = new ArrayList<>();
        List<Double> valuesForLeft = new ArrayList<>();
        List<Double> valuesForRight = new ArrayList<>();


        for (Map.Entry<Point, Square> squareEntry : stateImplementation.getSquares().entrySet()) {
            Point squarePosition = squareEntry.getKey();

            Point circlePosition = circlePointMap.get(squareEntry.getValue().getColor());

            Double valueX = squarePosition.getX() - circlePosition.getX();
            Double valueY = squarePosition.getY() - circlePosition.getY();

            if(valueX > 0)
                valuesForLeft.add(valueX);
            else if(valueX < 0)
                valuesForRight.add(Math.abs(valueX));

            if(valueY > 0)
                valuesForUp.add(valueY);
            else if(valueY < 0)
                valuesForDown.add(Math.abs(valueY));

        }

        Double result = 0.0;

        if (!valuesForUp.isEmpty())
            result += Collections.max(valuesForUp);

        if(!valuesForDown.isEmpty())
            result += Collections.max(valuesForDown);

        if(!valuesForLeft.isEmpty())
            result += Collections.max(valuesForLeft);

        if(!valuesForRight.isEmpty())
            result += Collections.max(valuesForRight);

        return result.intValue();
    }
}
