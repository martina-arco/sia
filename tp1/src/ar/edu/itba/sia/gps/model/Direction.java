package ar.edu.itba.sia.gps.model;

public enum Direction {
    UP, RIGHT, DOWN, LEFT;

    public String toStringCustom() {
        switch (this) {
            case UP:
                return "↑";
            case DOWN:
                return "↓";
            case LEFT:
                return "←";
            case RIGHT:
                return "→";
        }
        return "";
    }
}
