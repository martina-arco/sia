package ar.edu.itba.sia.gps.model;


public class Circle extends Figure{

    public Circle(String color) {
        super(color);
    }

    @Override
    public String toString() {
        return getColor() + " C";
    }
}
