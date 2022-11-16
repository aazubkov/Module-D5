# >>> c4 = Comment.objects.all()[3]
# >>> auth1 = Author.objects.all()[0]

# def change_rating(self, d):
#     if self.rating > 5:
#         raise LikeError('Слишком много лайков, похоже на спам-атаку!')
#     else:
#         self.rating += d
#         self.save()
#
#
# def like(self):
#     try:
#         self.change_rating(1)
#     except LikeError as e:
#         print(f'Ошибочка вышла: {e}')
#
#
# def dislike(self):
#     self.change_rating(-1)