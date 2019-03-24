package ar.edu.itba.sia.gps.model;

import java.awt.*;

public class Square extends Figure{

    private Direction direction;

    public Square(String color, Direction direction, Point position) {
        super(color, position);
        this.direction = direction;
    }


    public Direction getDirection() {
        return direction;
    }


    public void setDirection(Direction direction) {
        this.direction = direction;
    }

    public boolean equals(Square s) {
        return s.getColor().equals(getColor()) && s.getDirection().equals(getDirection());
    }

}
