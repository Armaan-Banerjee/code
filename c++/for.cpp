#include<iostream>
#include<vector>

int product(const std::vector<int>& items) {
    auto result = 1;

    for (auto it = items.cbegin(); it != items.cend(); ++it){
        result *= *it;
    }

    return result;
}

int main() {
    std::vector<int> vect(1, 2);

    int res = product(vect);
    std::cout << res;
}
