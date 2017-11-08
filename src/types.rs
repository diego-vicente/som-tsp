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

/// A neuron is located in the map and contains reference to the city that is
/// closer to it (the winner).
pub struct Neuron {
    pub x: f32,
    pub y: f32,
    pub winner: Option<City>,
}

impl Locatable for Neuron {
    fn get_location(&self) -> (f32, f32) {
        (self.x, self.y)
    }
}

/// The network is formed by a sequential, wrapping on the edges vector of
/// neurons.
pub struct Network {
    pub vec: Vec<Neuron>,
}

impl Network {
    /// Get a reference to the next neuron of a given index in a network,
    /// taking into account the ring shape and wrapping the edges.
    pub fn get_next(&self, idx: usize) -> &Neuron {
        &self.vec[(idx + 1) % self.vec.len()]
    }

    /// Get a reference to the previous neuron of a given index in a network,
    /// taking into account the ring shape and wrapping the edges.
    pub fn get_prev(&self, idx: usize) -> &Neuron {
        &self.vec[(idx as isize - 1) as usize % self.vec.len()]
    }
}
