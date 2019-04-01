package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.*;

public class RuleImpl implements Rule {

    private Square squareToMove;

    public RuleImpl(Square squareToMove) {
        this.squareToMove = squareToMove;
    }

    @Override
    public Integer getCost() {
        return 1;
    }

    @Override
    public String getName() {
        return "You moved the " + squareToMove.getColor() + " square " + squareToMove.getDirection().toString().toLowerCase() + ".";
    }

    @Override
    public Optional<State> apply(State state) {
        StateImpl stateImplementation = (StateImpl) state;
        Map<Point, Square> newSquareMap = new HashMap<>(stateImplementation.getSquares());

        Point newPosition = moveSquare(squareToMove, newSquareMap, stateImplementation.getDimension());

        if(newPosition == null)
            return Optional.empty();

        return Optional.of(new StateImpl(newSquareMap, stateImplementation.getCircles(), stateImplementation.getDimension()));

    }

    private Point moveSquare(Square square, Map<Point, Square> squareMap, int dimension) {

        Point newPosition = new Point();
        Point currentPosition = new Point();

        for (Map.Entry<Point, Square> entry:squareMap.entrySet()) {
            if(square.getColor().equals(entry.getValue().getColor()))
                currentPosition = entry.getKey();
        }

        Double currentX = currentPosition.getX();
        Double currentY = currentPosition.getY();

        switch (squareToMove.getDirection()) {
            case UP:
                newPosition.move(currentX.intValue() - 1, currentY.intValue());
                break;
            case DOWN:
                newPosition.move(currentX.intValue() + 1, currentY.intValue());
                break;
            case LEFT:
                newPosition.move(currentX.intValue(), currentY.intValue() - 1);
                break;
            case RIGHT:
                newPosition.move(currentX.intValue(), currentY.intValue() + 1);
                break;

        }

        if(newPosition.getX() >= 0 && newPosition.getY() >= 0 && newPosition.getX() < dimension && newPosition.getY() < dimension) {

            Square squareToPush = squareMap.get(newPosition);

            if(squareToPush != null)
                newPosition = moveSquare(squareToPush, squareMap, dimension);

            if(newPosition != null) {

                Square square1 = new Square(square.getColor(), square.getDirection());
                squareMap.put(newPosition, square1);
                squareMap.remove(currentPosition);

                return currentPosition;
            }
        }

        return null;
    }


}
