extern crate tsplib;
use self::tsplib::NodeCoord::Two;
use std::fs::File;
use std::io::BufReader;

pub struct City {
    id: usize,
    x: f32,
    y: f32,
}

/// Read a file containing the information of a map with cities.
pub fn read_cities(path: String) -> Result<Vec<City>, String> {
    let file = File::open(path).unwrap();
    let raw_data = tsplib::parse(BufReader::new(file));
    let triples = match raw_data.unwrap().node_coord {
        Some(data) => {
            // TODO: Allow for three dimensional TSP?
            match data {
                Two(cities) => cities,
                _ => panic!("Number of dimensions not supported"),
            }
        }
        None => panic!("No cities found in the given file"),
    };

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

    return Ok(cities);
}
