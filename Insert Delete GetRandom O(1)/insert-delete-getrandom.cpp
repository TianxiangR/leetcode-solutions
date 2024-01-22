#include <bits/stdc++.h>

using namespace std;

class RandomizedSet {
private:
  unordered_map<int, size_t> m;
  vector<int> v;
  random_device rd;
  mt19937 gen;

public:
    RandomizedSet() {
      gen = mt19937(rd());
    }
    
    bool insert(int val) {
        if (m.find(val) != m.end())
        {
          // we have already had this in the set
          return false;
        }

        m[val] = v.size();
        v.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (m.find(val) == m.end())
        {
          // if there's no such element in the set
          return false;
        }
        
        int idx = m[val];
        swap(m[val], m[v.back()]);
        swap(v.back(), v[idx]);
        v.pop_back();
        m.erase(val);

        return true;
    }
    
    int getRandom() {
        uniform_int_distribution<int> discrete_distribution(0, v.size() - 1);
        int random_number = discrete_distribution(gen);

        return v[random_number];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */

int main()
{
  RandomizedSet rs;
  rs.insert(0);
  rs.insert(1);
  rs.remove(0);
  rs.insert(2);
  rs.remove(1);
  cout << rs.getRandom() << endl;
}
