from auto_factory import AutoFactory

factory = AutoFactory()

for car_name in 'DodgeSRT', 'Tesla', 'Chevrolet':
    car = factory.create_instance(car_name)

    car.start()
    car.stop()
    print('----------------')

print('\n')

from factories import loader

for factory_name in 'dodge_factory', 'tesla_factory', 'chevrolet_factory':
    factory = loader.load_factory(factory_name)
    car = factory.create_auto()

    car.start()
    car.stop()
    print('----------------')
