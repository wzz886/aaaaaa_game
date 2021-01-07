-- -- for CCLuaEngine traceback
-- function __G__TRACKBACK__(msg)
-- 	print(msg, Log(debug.traceback()))
-- end

-- local status, msg = xpcall(Main, __G__TRACKBACK__)
-- if not status then
--     error(msg)
-- end


print("ok")

-- 自动增加物品 要删
-- local item_list = {}
-- item_list.Count = 0

-- local i = 0
-- for k, v in pairs(ItemConfig.info) do
-- 	if i < 20 then
-- 		item_list[i] = {itemId = v.bid, count = i * 10 + 1, objectId = i + 1}
-- 		i = i + 1
-- 		item_list.Count = item_list.Count + 1
-- 	end
-- end

-- EventManager:sendMsg(EVENT.BAG.R_ALL_ITEM_DATA, item_list)
