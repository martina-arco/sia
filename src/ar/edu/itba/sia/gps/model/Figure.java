package ar.edu.itba.sia.gps.model;

import java.awt.*;

public class Figure {

    private String color;

    private Point position;

    public Figure(String color, Point position) {
        this.color = color;
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
}
