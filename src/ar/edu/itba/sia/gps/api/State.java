package ar.edu.itba.sia.gps.api;

import ar.edu.itba.sia.gps.model.Circle;
import ar.edu.itba.sia.gps.model.Figure;
import ar.edu.itba.sia.gps.model.Square;

import java.awt.*;
import java.util.List;
import java.util.Map;

/**
 * State interface.
 */
public interface State {

	/**
	 * Compares self to another state to determine whether they are the same or not.
	 * 
	 * @param state
	 *            The state to compare to.
	 * @return true if self is the same as the state given, false if they are different.
	 */
	boolean equals(Object state);

	/**
	 * Provides the representation of the state so it can be printed on the solution representation.
	 *
	 * @return The STRING representation of the state.
	 */
	String getRepresentation();

	Map<Point, Square> getSquares();

	Map<Point, Circle> getCircles();

	int getDimension();

}
