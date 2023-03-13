import * as Joi from 'joi';


export const RabbitMQSchema = {
    RABBIT_MQ_URI: Joi.string().required()
}