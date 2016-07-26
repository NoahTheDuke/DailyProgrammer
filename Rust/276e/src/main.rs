use std::env;

fn main() {
    let args: Vec<_> = env::args().collect();
    let mut word: String;
    let width: i32;
    let height: i32;

    if args.len() > 1 {
        word = args[1].to_string();
        width = args[2].parse().unwrap();
        height = args[3].parse().unwrap();
    } else {
        word = "rekt".to_string();
        width = 1;
        height = 1;
    }

    word = word.to_uppercase();

    let rec_width = word.len() as i32 * width - (width - 1);
    let rec_height = word.len() as i32 * height - (height - 1);

    let mut v = vec![vec![" ".to_string(); rec_width as usize]; rec_height as usize];

    for x in 0..width as usize {
        for y in 0..height as usize {
            let mut w: String;
            let rx: usize = y * (word.len() - 1);
            let ry: usize = x * (word.len() - 1);

            if (x + y) % 2 == 0 {
                w = word.clone();
            } else {
                w = word.chars().rev().collect::<String>();
            }

            for i in 0..word.len() as usize {
                v[0 + rx][i + ry] = w.chars().nth(i).unwrap().to_string();
                v[i + rx][0 + ry] = w.chars().nth(i).unwrap().to_string();
                v[w.len()- 1 + rx][i + ry] = w.chars().nth(w.len() - 1 - i).unwrap().to_string();
                v[i + rx][w.len() - 1 + ry] = w.chars().nth(w.len() - 1 - i).unwrap().to_string();
            }
        }
    }
    for line in v {
        for c in line {
            print!("{}", c);
        }
        print!("\n");
    }
}
