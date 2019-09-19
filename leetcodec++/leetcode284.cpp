//
// Created by 黄敏辉 on 2019-09-18.
//

// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.

class Iterator {
    struct Data;
    Data* data;
public:
    Iterator(const vector<int>& nums);
    Iterator(const Iterator& iter);
    virtual ~Iterator();
    // Returns the next element in the iteration.
    int next();
    // Returns true if the iteration has more elements.
    bool hasNext() const;
};


class PeekingIterator : public Iterator {
private:
    int m_next;
    bool m_hasnext = false;
public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        // Initialize any member here.
        // **DO NOT** save a copy of nums and manipulate it directly.
        // You should only use the Iterator interface methods.
        m_hasnext = Iterator::hasNext();
        if(m_hasnext)
            m_next = Iterator::next();

    }

    // Returns the next element in the iteration without advancing the iterator.
    int peek() {
        return m_next;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    int next() {
        int tmp = m_next;
        m_hasnext = Iterator::hasNext();
        if(m_hasnext)
            m_next = Iterator::next();
        return tmp;
    }

    bool hasNext() const {
        return m_hasnext;
    }
};