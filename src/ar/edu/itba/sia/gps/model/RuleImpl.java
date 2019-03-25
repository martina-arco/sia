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
        return "You moved the " + squareToMove.getColor() + " square " + squareToMove.getDirection() + ".";
    }

    @Override
    public Optional<State> apply(State state) {
        Map<Point, Square> currentSquares = state.getSquares();
        Map<Point, Square> newSquareMap = new HashMap<>(currentSquares);

        Point newPosition = moveSquare(squareToMove, currentSquares, newSquareMap, state.getDimension());

        if(newPosition == null)
            return Optional.empty();

        pushAdjacentSquare(newPosition, currentSquares, newSquareMap, state.getDimension());

        return Optional.of(new StateImpl(newSquareMap, state.getCircles(), state.getDimension()));

    }

    private Point moveSquare(Square square, Map<Point, Square> currentMap, Map<Point, Square> newSquareMap, int dimension) {

        Point newPosition = new Point();

        Point currentPosition = currentMap.entrySet()
                .stream()
                .filter(entry -> square.equals(entry.getValue()))
                .map(Map.Entry::getKey).findFirst().get();

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

            Square square1 = new Square(square.getColor(), square.getDirection());

            newSquareMap.put(newPosition, square1);
            newSquareMap.remove(currentPosition);

            return newPosition;
        }


        return null;
    }

    private void pushAdjacentSquare(Point newPosition, Map<Point, Square> currentMap, Map<Point, Square> newSquareMap, int dimension) {

        Square squareToPush = currentMap.get(newPosition);

        if(squareToPush != null) {
            newPosition = moveSquare(squareToPush, currentMap, newSquareMap, dimension);
            pushAdjacentSquare(newPosition, currentMap, newSquareMap, dimension);
            currentMap.put(newPosition, squareToPush);
        }

    }
}
