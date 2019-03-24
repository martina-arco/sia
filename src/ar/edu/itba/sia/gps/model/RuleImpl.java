package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

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
        return "Moviste el cuadrado de color " + squareToMove.getColor() + " en la direccion " + squareToMove.getDirection();
    }

    @Override
    public Optional<State> apply(State state) {

        Optional<State> stateResult = Optional.ofNullable(state);
        List<Square> squares = stateResult.get().getSquares();
        Map<Point, Square> squarePositionMap = squares.stream().collect(Collectors.toMap(Square::getPosition, square->square));

        Point newPosition = moveSquare(squareToMove);

        pushAdjacentSquare(newPosition, squarePositionMap);

        return stateResult;

    }

    private Point moveSquare(Square square) {

        Point newPosition = new Point();

        Double currentX = square.getPosition().getX();
        Double currentY = square.getPosition().getY();

        switch (square.getDirection()) {
            case UP:
                newPosition.move(currentX.intValue(), currentY.intValue() + 1);
                break;
            case DOWN:
                newPosition.move(currentX.intValue(), currentY.intValue() - 1);
                break;
            case LEFT:
                newPosition.move(currentX.intValue() - 1, currentY.intValue());
                break;
            case RIGHT:
                newPosition.move(currentX.intValue() + 1, currentY.intValue());
                break;

        }

        square.setPosition(newPosition);

        return newPosition;
    }

    private void pushAdjacentSquare(Point newPosition, Map<Point, Square> squarePositionMap) {

        Square squareToPush = squarePositionMap.get(newPosition);

        if(squareToPush != null) {
            newPosition = moveSquare(squareToPush);
            pushAdjacentSquare(newPosition, squarePositionMap);
        }

    }
}
