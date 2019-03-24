package ar.edu.itba.sia.gps.model;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class StateImpl implements State {

    private List<Square> squares;
    private List<Circle> circles;

//    todavia no se si lo necesito
    private List<Point> positionsOccupiedBySquares;


    public StateImpl(List<Square> squares, List<Circle> circles) {
        this.squares = squares;
        this.circles = circles;
    }

    public List<Point> getPositionsOccupiedBySquares() {
        return positionsOccupiedBySquares;
    }

    @Override
    public String getRepresentation() {
        return null;
    }

    public List<Square> getSquares() {
        return squares;
    }

    public List<Circle> getCircles() {
        return circles;
    }
}
