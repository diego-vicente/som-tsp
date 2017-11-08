extern crate tsplib;
use super::types::{City, Problem};

use self::tsplib::NodeCoord::Two;
use std::fs::File;
use std::io::BufReader;

/// Read a file containing the information of a map with cities.
pub fn read_cities(path: String) -> Problem {
    let file = File::open(path).unwrap();
    let raw_data = tsplib::parse(BufReader::new(file)).unwrap();
    let triples = match raw_data.node_coord {
        Some(Two(cities)) => cities,
        // TODO: Accept 3 dimensional problems?
        _ => panic!("No adequate cities found in the given file"),
    };

    let name = raw_data.name;

    let cities = triples
        .iter()
        .map(|triple| {
            City {
                id: triple.0,
                x: triple.1,
                y: triple.2,
            }
        })
        .collect();

    return Problem {
        name: name,
        cities: cities,
    };
}
