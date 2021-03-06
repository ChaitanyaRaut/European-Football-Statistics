import sqlobject
from sqlobject import SQLObjectNotFound


def get_transaction():
    connect = sqlobject.sqlhub.getConnection()
    transaction = connect.transaction()
    return transaction

def commit_transaction(transaction, close_transaction):
    transaction.commit(close=close_transaction)

def rollback_transaction(transaction):
    transaction.rollback()


class baseDLobject():
    def __init__(self, table_cls):
        # Given the current DL uses SQLObject the input table_cls is supposed to be a sqlobject.SQLObject derived class
        self.table_cls = table_cls
        self.fields = self.table_cls.sqlmeta.columns.keys()
        #self.sqlcolumns = self.table_cls.sqlmeta.columnList
        #self.db_column_names = [self.table_cls.sqlmeta.idName] + [col.dbName for col in self.sqlcolumns]

    def _create(self, **kwargs):
        row = self.table_cls(**kwargs)
        return self._as_dict(row)

    def _as_dict(self, row):
        d =  dict((c,getattr(row, c)) for c in self.fields)
        d['id'] = row.id
        return d

    def _update(self, row_id, **kwargs):
        row = self._get_row_sqlobj(row_id)
        row.set(**kwargs)
        return self._as_dict(row)

    def _get_row_sqlobj(self, row_id, transaction=None):
        try:
            row = self.table_cls.get(row_id, connection=transaction)
        except SQLObjectNotFound as fault:
            raise fault

        if not row:
            raise Exception         #TODO Handle different cases of exceptions
        return row

    def _update_using_transaction(self, row_id, transaction, **kwargs):
        try:
            row = self.table_cls.select(self.table_cls.q.id==row_id, connection = transaction).getOne()
            row.set(**kwargs)
            return self._as_dict(row)
        except Exception as fault:
            raise fault

    def _create_where_clause(self, row_id):
        where_expr = self.table_cls.q.id == row_id
        return where_expr

    def _delete_row(self, row_id, **kwargs):
        if kwargs.get('connection', None):
            row = self.table_cls.select(self.table_cls.q.id==row_id, connection=kwargs['connection']).getOne()
        else:
            row = self.table_cls.select(self.table_cls.q.id==row_id).getOne()

        self._destroy_row_sqlobj(row)
        return True

    def _destroy_row_sqlobj(self, row):
        row.destroySelf()
        row.expire()
        row = NoneObj()

    def _count(self, **kwargs):
        rows = self.table_cls.selectBy(**kwargs)
        return rows.count()

    def _listby(self, **kwargs):
        rows = self.table_cls.selectBy(**kwargs)
        if "connection" in kwargs:
            return [self._as_dict(r) for r in rows]
        return self._rows_as_dict(rows)