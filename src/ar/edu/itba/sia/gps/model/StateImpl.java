package ar.edu.itba.sia.gps.model;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class StateImpl implements State {

    private List<Square> squares;
    private List<Circle> circles;


    public StateImpl(List<Square> squares, List<Circle> circles) {
        this.squares = squares;
        this.circles = circles;
    }

    @Override
    public String getRepresentation() {
        return null;
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
