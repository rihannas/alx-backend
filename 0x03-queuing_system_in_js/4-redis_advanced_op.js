import * as redis from 'redis';
const redisClient = redis.createClient();

redisClient.connect()

const KEY = 'HolbertonSchools';

const feilds = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

feilds.forEach((key, index) => {
    redisClient.HSET(KEY, feilds, values[index], redis.print);
});

redisClient.HGETALL(KEY, (err, value) => {
    console.log(value);
});
