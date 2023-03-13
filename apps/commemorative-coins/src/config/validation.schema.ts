import * as Joi from 'joi';
import { RabbitMQSchema } from '@/validation';


export const validationSchema = Joi.object({
    ...RabbitMQSchema,
});