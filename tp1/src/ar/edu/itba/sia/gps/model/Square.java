package ar.edu.itba.sia.gps.model;

import java.util.Objects;

public class Square extends Figure{

    private Direction direction;

    public Square(String color, Direction direction) {
        super(color);
        this.direction = direction;
    }

    public Direction getDirection() {
        return direction;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Square)) return false;
        Square square = (Square) o;
        return super.equals(o) && getDirection() == square.getDirection();
    }

    @Override
    public int hashCode() {
        return Objects.hash(getDirection(), getColor());
    }


    @Override
    public String toString() {
        return getColor() + " S " + getDirection().toStringCustom();
    }
}
