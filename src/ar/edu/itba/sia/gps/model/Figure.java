package ar.edu.itba.sia.gps.model;

import java.awt.*;

public class Figure {

    private String color;

    private Point position;

    public Figure(String color, Point position) {
        this.color = color;
        this.position = position;
    }

    public String getColor() {
        return color;
    }

    public Point getPosition() {
        return position;
    }

    public void setPosition(Point position) {
        this.position = position;
    }

    @Override
    public String toString() {
        return "color='" + color + '\'' +
                ", position=(" + position.getX()+", " + position.getY() + " )";
    }
}
