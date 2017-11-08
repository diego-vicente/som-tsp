pub mod io;
pub mod distances;
pub mod types;

fn main() {
    let problem = io::read_cities(String::from("assets/qa194.tsp"));

    println!("Problem read: {}", problem.name);
    for city in problem.cities.iter() {
        println!("City #{} at ({}, {})", city.id, city.x, city.y)
    }

    println!(
        "Test distance: ({}, {}) to ({}, {}) is {}",
        problem.cities[0].x,
        problem.cities[0].y,
        problem.cities[1].x,
        problem.cities[1].y,
        distances::euclidean(&problem.cities[0], &problem.cities[1])
    )
}
