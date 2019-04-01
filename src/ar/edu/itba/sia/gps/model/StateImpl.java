package ar.edu.itba.sia.gps.model;
import ar.edu.itba.sia.gps.api.State;

import org.apache.commons.lang.StringUtils;


import java.awt.*;
import java.util.Map;
import java.util.Objects;

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
        addNewLine(sbuilder);

        for (int i = 0; i < dimension; i++) {

            sbuilder.append("|");

            for (int j = 0; j < dimension; j++) {
                Point point = new Point(i, j);
                Square square = squares.get(point);
                Circle circle = circles.get(point);


                if(square != null && circle != null) {

                    addElement(sbuilder, circle.toString() + " " + square.toString());

                } else if(circle == null && square == null) {

                    addElement(sbuilder, "0");

                } else {
                        if (square != null)
                            addElement(sbuilder, square.toString());

                        if (circle != null)
                            addElement(sbuilder, circle.toString());
                }

                sbuilder.append("|");
            }

            addNewLine(sbuilder);

        }
        return sbuilder.toString();
    }

    private void addElement(StringBuilder sbuilder, String element) {
        sbuilder.append(String.format("%20s", StringUtils.center(element, 20)));
    }

    private void addNewLine(StringBuilder sbuilder) {
        sbuilder.append("\n");
        sbuilder.append(new String(new char[dimension*21]).replace("\0", "-"));
        sbuilder.append("\n");
    }

    public Map<Point, Square> getSquares() {
        return squares;
    }

    public Map<Point, Circle> getCircles() {
        return circles;
    }

    public int getDimension() {
        return dimension;
    }

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
