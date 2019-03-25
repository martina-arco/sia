package ar.edu.itba.sia.gps.model;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class StateImpl implements State {

    private List<Square> squares;
    private List<Circle> circles;
    private int dimension;

    public StateImpl(List<Square> squares, List<Circle> circles, int dimension) {
        this.squares = squares;
        this.circles = circles;
        this.dimension = dimension;
    }

    @Override
    public String getRepresentation() {

        Map<Point, Square> squarePositions =  squares.stream().collect(Collectors.toMap(Square::getPosition, square->square));
        Map<Point, Circle> circlePositions = circles.stream().collect(Collectors.toMap(Circle::getPosition, circle->circle));

        StringBuilder sbuilder = new StringBuilder();

        sbuilder.append("State : \n");

        for (int i = 0; i < dimension; i++) {
            for (int j = 0; j < dimension; j++) {
                Point point = new Point(i, j);
                Square square = squarePositions.get(point);
                Circle circle = circlePositions.get(point);
                if(square != null) {
                    sbuilder.append(square.toString());
                }
                if(circle != null) {
                    sbuilder.append(circle.toString());
                }
                if(circle == null && square == null)
                    sbuilder.append("0");

                sbuilder.append(", ");
            }
            sbuilder.append("\n");
        }
        return sbuilder.toString();
    }

    @Override
    public List<Square> getSquares() {
        return squares;
    }

    @Override
    public List<Circle> getCircles() {
        return circles;
    }
}
