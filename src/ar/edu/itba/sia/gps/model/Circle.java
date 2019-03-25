package ar.edu.itba.sia.gps.model;

import java.awt.*;

public class Circle extends Figure{

    public Circle(String color) {
        super(color);
    }

    @Override
    public String toString() {
        return getColor() + "C ";
    }
}
