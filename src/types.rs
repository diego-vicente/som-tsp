use distances::Locatable;

/// A city representation in a 2D plane.
pub struct City {
    pub id: usize,
    pub x: f32,
    pub y: f32,
}

impl Locatable for City {
    fn get_location(&self) -> (f32, f32) {
        (self.x, self.y)
    }
}

/// A problem has a name and a list of cities to be routed.
pub struct Problem {
    pub name: String,
    pub cities: Vec<City>,
    // TODO: Include optimal route/distance?
}
