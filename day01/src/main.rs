
fn main() {
    // start by reading the input file as a vec of strings
    let input = std::fs::read_to_string("input.txt").unwrap();
    let input: Vec<&str> = input.lines().collect();

    // split the vec by a blank line
    let mut groups: Vec<Vec<&str>> = Vec::new();
    let mut group: Vec<&str> = Vec::new();
    for line in input {
        if line == "" {
            groups.push(group);
            group = Vec::new();
        } else {
            group.push(line);
        }
    }
    groups.push(group);

    // sum each group
    let mut sums = Vec::<i32>::new();
    for group in groups {
        let mut sum = 0;
        for line in group {
            sum += line.parse::<i32>().unwrap();
        }
        sums.push(sum);
    }

    // part 1 wants the max
    println!("Part 1: {}", sums.iter().max().unwrap());

    // part 2 wants the sum of the top 3 numbers
    sums.sort();
    sums.reverse();
    println!("Part 2: {}", sums[0] + sums[1] + sums[2]);
}
