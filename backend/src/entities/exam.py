# coding=utf-8

from marshmallow import Schema, fields


# ... other import statements ...

# ... Exam class definition ...

class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
