import coreapi
import coreschema
from rest_framework.schemas import AutoSchema, ManualSchema
DeleteSceneSchema = AutoSchema(
    [
        coreapi.Field(
            name="sce_id",#单个删除
            required=True,
            location="form",
            #schema=coreschema.Array(),多个用户删除操作用数组
            schema=coreschema.Integer(),
            description="场景ID",
        )
    ]
)