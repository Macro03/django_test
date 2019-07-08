import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema
DeleteUserSchema = AutoSchema(
    [
        coreapi.Field(
            name="user_id",#单个删除
            required=True,
            location="form",
            #schema=coreschema.Array(),多个用户删除操作用数组
            schema=coreschema.Integer(),
            description="用户ID列表",
        )
    ]
)
#根据需要增加删除条件
'''        
       coreapi.Field(
           name="user_name",#单个删除
           required=True,
           location="form",
           #schema=coreschema.Array(),多个用户删除操作用数组
           schema=coreschema.String(),
           description="用户名字列表",
       )
'''