package ar.edu.itba.sia.gps.model;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

public class StateImpl implements State {

    private Map<Point, Square> squares;
    private Map<Point, Circle> circles;
    private int dimension;

    public StateImpl(Map<Point, Square> squares, Map<Point, Circle> circles, int dimension) {
        this.squares = squares;
        this.circles = circles;
        this.dimension = dimension;
    }

    @Override
    public String getRepresentation() {

        StringBuilder sbuilder = new StringBuilder();

        sbuilder.append("State : \n");

        for (int i = 0; i < dimension; i++) {
            for (int j = 0; j < dimension; j++) {
                Point point = new Point(i, j);
                Square square = squares.get(point);
                Circle circle = circles.get(point);
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
    public Map<Point, Square> getSquares() {
        return squares;
    }

    @Override
    public Map<Point, Circle> getCircles() {
        return circles;
    }

    public int getDimension() {
        return dimension;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof StateImpl)) return false;
        StateImpl state = (StateImpl) o;
        return dimension == state.dimension &&
                getSquares().equals(state.getSquares()) &&
                getCircles().equals(state.getCircles());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getSquares(), getCircles(), dimension);
    }
}
