package ar.edu.itba.sia.gps.model;

import ar.edu.itba.sia.gps.api.Rule;
import ar.edu.itba.sia.gps.api.State;

import java.awt.*;
import java.util.List;
import java.util.Optional;

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

        boolean squareFound = false;

        for (int i = 0; i < squares.size() && !squareFound; i++) {
            Square square = squares.get(i);

            if(square.equals(this.squareToMove)) {

                Double currentX = square.getPosition().getX();
                Double currentY = square.getPosition().getY();
                Point newPosition = new Point();

//                TO DO falta lo de empujar cuadrados

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

                squareFound = true;
            }
        }


        return stateResult;

    }
}
