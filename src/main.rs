pub mod io;
pub mod types;

fn main() {
    let problem = io::read_cities(String::from("assets/qa194.tsp"));

    println!("Problem read: {}", problem.name);
    for city in problem.cities.iter() {
        println!("City #{} at ({}, {})", city.id, city.x, city.y)
    }
}
