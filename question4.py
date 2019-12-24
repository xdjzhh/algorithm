'''
这个题的本质是找寻 create_at = '2018-11-11' 的商品中ID最大的记录（期末库存就是最后记录的ID）

select product_id,max(id),create_at from storage_record where create_at = '2018-11-11' group by product_id;
'''