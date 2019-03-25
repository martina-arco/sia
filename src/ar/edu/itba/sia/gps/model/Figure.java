package ar.edu.itba.sia.gps.model;

import java.util.Objects;

public class Figure {

    private String color;

    public Figure(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return "color='" + color;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Figure)) return false;
        Figure figure = (Figure) o;
        return getColor().equals(figure.getColor());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getColor());
    }
}
