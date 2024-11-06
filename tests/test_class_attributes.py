class Base:
    class_attr = 1


def test_class_attributes() -> None:

    assert Base.class_attr == 1

    # Change class attribute
    Base.class_attr = 2
    assert Base.class_attr == 2

    # Create an instance
    obj1 = Base()
    assert obj1.class_attr == 2

    obj2 = Base()
    assert obj2.class_attr == 2

    # Change base class attribute
    Base.class_attr = 3
    assert Base.class_attr == 3

    assert obj1.class_attr == 3
    assert obj2.class_attr == 3

    # Change instance attribute
    obj1.class_attr = 4
    assert obj1.class_attr == 4

    assert obj2.class_attr == 3
    assert Base.class_attr == 3
