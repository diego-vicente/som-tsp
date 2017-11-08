pub trait Locatable {
    fn get_location(&self) -> (f32, f32);
}

/// Compute the distance in a straight line between two Locatable objects.
pub fn euclidean<T, U>(a: &T, b: &U) -> f32
where
    T: Locatable,
    U: Locatable,
{
    let (x_a, y_a) = a.get_location();
    let (x_b, y_b) = b.get_location();

    {
        let delta_x = x_a - x_b;
        let delta_y = y_a - y_b;

        delta_x * delta_x + delta_y * delta_y
    }.sqrt()
}
