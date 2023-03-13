import * as Joi from 'joi';


export const DatabaseSchema = {
    DB_HOST:     Joi.string().required(),
    DB_PORT:     Joi.number().required(),
    DB_USERNAME: Joi.number().required(),
    DB_PASSWORD: Joi.number().required(),
    DB_DATABASE: Joi.number().required(),
}