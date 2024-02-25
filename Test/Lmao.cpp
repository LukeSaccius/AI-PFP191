#include <iostream>
#include <vector>
#include <random>

int main()
{
    const int sequence_size = 10; // Size of the sequence
    const int range_from = 1;     // Start of range (inclusive)
    const int range_to = 10;      // End of range (inclusive)
    const int search_for = 2;     // Value to search for

    std::random_device rand_dev;        // Seed for the random number engine
    std::mt19937 generator(rand_dev()); // Standard mersenne_twister_engine seeded with rand_dev()
    std::uniform_int_distribution<int> distr(range_from, range_to);

    std::vector<int> a(sequence_size);

    // Generate random sequence
    for (int &num : a)
    {
        num = distr(generator);
    }

    // Print the random sequence
    std::cout << "Random Sequence: ";
    for (const int &num : a)
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Find and print indices of 'search_for'
    std::cout << "Indices of " << search_for << ": ";
    for (size_t i = 0; i < a.size(); ++i)
    {
        if (a[i] == search_for)
        {
            std::cout << i << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}
